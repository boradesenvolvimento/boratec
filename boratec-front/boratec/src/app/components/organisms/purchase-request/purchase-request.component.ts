import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { AdminToolsService } from 'src/app/services/admin-tools.service';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';

declare const $: any;

@Component({
  selector: 'app-purchase-request',
  templateUrl: './purchase-request.component.html',
  styleUrls: ['./purchase-request.component.scss']
})
export class PurchaseRequestComponent implements OnInit {
  error: any;
  purchases: any;
  showlist: boolean = false;

  constructor(
    private adminService: AdminToolsService,
    private router: Router,
  ) {}
  // DATA TABLE SETTINGS
  @ViewChild(DataTableDirective, {static: false})
  dtElement: DataTableDirective | undefined;

  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject();


  ngOnInit(): void {
    this.fetchPurchases()
    this.dtOptions = {
      dom: 'Bfrtip',
      pagingType: 'full_numbers',
      pageLength: 5,
    }
    console.log(this.purchases)
    this.dtTrigger.next(null)
  }

  ngAfterViewInit(): void {
    this.dtTrigger.next(null);
  }

  ngOnDestroy(): void {
    // Do not forget to unsubscribe the event
    this.dtTrigger.unsubscribe();
  }

  rerender(): void {
    this.dtElement?.dtInstance.then((dtInstance: DataTables.Api) => {
      // Destroy the table first
      dtInstance.destroy();
      // Call the dtTrigger to rerender again
      this.dtTrigger.next(null);
    });
  }

  importPurchase(request_id: string, company: string, branch: string){
    this.adminService.importPurchaseRequest(request_id, company, branch).subscribe(
      {
        error: (error) => this.error = error,
        complete: () => console.log('Complete')
      }
    )
  }

  fetchPurchases(){
    this.adminService.fetchPurchasesRequest().subscribe(
      {
        next: (success) => this.purchases = success,
        error: (error) => this.error = error,
        complete: () => this.showlist = true,
      }
    )
  }

}
