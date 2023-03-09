from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from adm_tools.models import PurchaseRequest
from .serializers import PurchaseRequestSerializer
from .services import conndb, dictfetchall, get_branch

from cx_Oracle import DatabaseError as cxerr

# Create your views here.

class PurchaseRequest(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseRequestSerializer

    def post(self, request: Request):
        request_id = request.data["request_id"]
        company = request.data["company"]
        branch = request.data["branch"]

        if request_id:
            conn = conndb()
            cur = conn.cursor()

            try:
                cur.execute(f"""
                            SELECT 
                                   SO.NUMEROSOLIC NR_SOLICITACAO,
                                   CM.DESCRICAOMAT PRODUTO,
                                   SO.DATASOLIC DATA,
                                   CIS.QTDEITSOLIC QTD_ITENS,
                                   CASE
                                       WHEN SO.STATUSSOLIC = 'A' THEN 'ABERTO'
                                       WHEN SO.STATUSSOLIC = 'P' THEN 'APROVADO'
                                       WHEN SO.STATUSSOLIC = 'F' THEN 'FECHADO'
                                   END STATUS,
                                   SO.CODIGOFL FILIAL,
                                   SO.USUARIO SOLICITANTE,
                                   CC.EMAIL
                            FROM
                                CPR_SOLICITACAO SO, 
                                CPR_ITENSSOLICITADOS CIS,
                                EST_CADMATERIAL CM,
                                CTR_CADASTRODEUSUARIOS CC
                            WHERE
                                    SO.CODIGOEMPRESA = {company}
                                AND
                                	SO.CODIGOFL = {branch}                  
                                AND
                                	SO.NUMEROSOLIC = CIS.NUMEROSOLIC 
                                AND
                                	SO.STATUSSOLIC = 'P'                      
                                AND    
                                	SO.DATASOLIC BETWEEN ((SYSDATE)-30) AND (SYSDATE) 
                                AND    
                                	CM.CODIGOMATINT = CIS.CODIGOMATINT                
                                AND
                                	SO.NUMEROSOLIC = {request_id}                        
                                AND
                                	CC.USUARIO = SO.USUARIO
                            GROUP BY
                                  SO.NUMEROSOLIC,
                                  CM.DESCRICAOMAT,
                                  SO.DATASOLIC,
                                  CIS.QTDEITSOLIC,
                                  SO.STATUSSOLIC,
                                  SO.CODIGOEMPRESA,
                                  SO.CODIGOFL,
                                  SO.USUARIO,
                                  CC.EMAIL
                            UNION ALL                        
                            SELECT 
                                   SO.NUMEROSOLIC NR_SOLICITACAO,
                                   SCO.DESCRICAOSOLOUTROS PRODUTO,
                                   SO.DATASOLIC DATA,
                                   SCO.QTDESOLOUTROS QTD_ITENS,
                                   CASE
                                       WHEN SO.STATUSSOLIC = 'A' THEN 'ABERTO'
                                       WHEN SO.STATUSSOLIC = 'P' THEN 'APROVADO'
                                       WHEN SO.STATUSSOLIC = 'F' THEN 'FECHADO'
                                   END STATUS,
                                   SO.CODIGOFL FILIAL,
                                   SO.USUARIO SOLICITANTE,
                                   CC.EMAIL
                            FROM
                                CPR_SOLICITACAO SO,
                                CPR_SOLICOUTROS SCO,
                                CTR_CADASTRODEUSUARIOS CC
                            WHERE
                                    SO.CODIGOEMPRESA = {company}
                                AND
                            		SO.CODIGOFL = {branch}                
                            	AND
                                	SO.NUMEROSOLIC = SCO.NUMEROSOLIC                  
                                AND
                                	SCO.STATUSSOLOUTROS = 'P'                         
                                AND    
                                	SO.DATASOLIC BETWEEN ((SYSDATE)-30) AND (SYSDATE) 
                                AND
                                	SO.NUMEROSOLIC = {request_id}                        
                                AND
                                	CC.USUARIO = SO.USUARIO                           
                            GROUP BY
                                  SO.NUMEROSOLIC,
                                  SCO.DESCRICAOSOLOUTROS,
                                  SCO.QTDESOLOUTROS,
                                  SO.DATASOLIC,
                                  SO.STATUSSOLIC,
                                  SO.CODIGOEMPRESA,
                                  SO.CODIGOFL,
                                  SO.USUARIO,
                                  CC.EMAIL
                            """)
            except cxerr:
                response = {"message": "Não foi encontrada essa solicitação"}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                response = {"message": "Erro ao buscar a solicitação", "error": e, "error_type": type(e).__name__}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            else:
                res = dictfetchall(cur)
                cur.close()
                if res:
                    print(res)
                    for p in res:
                        try:
                            purchase = PurchaseRequest.objects.get(request_id=p["nr_solicitacao"])
                        except ObjectDoesNotExist:
                            purchase = PurchaseRequest.objects.create(
                                request_id = p["nr_solicitacao"],
                                date = p["data"],
                                status = p["status"],
                                company = company,
                                branch_id = branch,
                                branch = get_branch(int(company), int(branch)),
                                category = p["category"],
                                requester = p["requester"],
                                requester_email = p["requester_email"],
                                author = request.user
                            )
                            product = PurchaseRequest.objects.create(
                                product=p["produto"],
                                itens_qty = int(p["qtd_itens"]),
                                solic_ref = purchase
                            )
                        else:
                            product = PurchaseRequest.objects.create(
                                product=p["produto"],
                                itens_qty = int(p["qtd_itens"]),
                                solic_ref = purchase
                            )
                            purchase.last_update = request.user
                            purchase.save()

                    response = {"message": "Solicitação cadastrada com sucesso!", "data": purchase}
                else:
                    response = {"message": "A solicitação não existe!"}
                    
        return Response(data=response, status=status.HTTP_200_OK)
    
    def get(self, request: Request):
    
        purchases = PurchaseRequest.objects.all()

        return Response(data=purchases, status=status.HTTP_200_OK)