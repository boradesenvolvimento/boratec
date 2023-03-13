import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './components/organisms/signup/signup.component';

import { AuthService, AuthInterceptor, AuthGuard } from './services/auth.service';
import { PurchaseRequestComponent } from './components/organisms/purchase-request/purchase-request.component';
import { LoginComponent } from './components/organisms/login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    PurchaseRequestComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
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
