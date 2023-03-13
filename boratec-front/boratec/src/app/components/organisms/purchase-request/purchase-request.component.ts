import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AdminToolsService } from 'src/app/services/admin-tools.service';

@Component({
  selector: 'app-purchase-request',
  templateUrl: './purchase-request.component.html',
  styleUrls: ['./purchase-request.component.scss']
})
export class PurchaseRequestComponent implements OnInit {
  error: any;

  constructor(
    private adminService: AdminToolsService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    
  }

  importPurchase(request_id: string, company: string, branch: string){
    this.adminService.importPurchaseRequest(request_id, company, branch).subscribe(
      {
        error: (error) => this.error = error,
        complete: () => console.log('Complete')
      }
    )
  }


}
