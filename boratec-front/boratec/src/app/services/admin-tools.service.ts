import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AdminToolsService {

  private apiRoot = 'http://127.0.0.1:8000/api/';

  constructor(private http: HttpClient) { }

  importPurchaseRequest(request_id: string, company: string, branch: string) {
    return this.http.post(
      this.apiRoot.concat('purchase_request/'),
      {
        "request_id": request_id,
        "company": company,
        "branch": branch
      }
    )
  }
}
