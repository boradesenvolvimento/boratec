import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './components/organisms/signup/signup.component';

import { OverlayModule } from '@angular/cdk/overlay';
import { CdkMenuModule } from '@angular/cdk/menu';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome'
import { DataTablesModule } from 'angular-datatables';


import { AuthService, AuthInterceptor, AuthGuard } from './services/auth.service';
import { PurchaseRequestComponent } from './components/organisms/purchase-request/purchase-request.component';
import { LoginComponent } from './components/organisms/login/login.component';
import { SidenavComponent } from './components/molecules/sidenav/sidenav.component';
import { ExtractCompanyPipe } from './components/atoms/extract-company.pipe';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    PurchaseRequestComponent,
    LoginComponent,
    SidenavComponent,
    ExtractCompanyPipe,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CdkMenuModule,
    OverlayModule,
    FontAwesomeModule,
    DataTablesModule
  ],
  providers: [
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    },
    
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
