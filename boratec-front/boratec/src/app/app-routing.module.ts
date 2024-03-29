import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccountComponent } from './components/organisms/account/account.component';
import { LoginComponent } from './components/organisms/login/login.component';
import { PurchaseRequestComponent } from './components/organisms/purchase-request/purchase-request.component';
import { SignupComponent } from './components/organisms/signup/signup.component';
import { AuthGuard } from './services/auth.service';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent},
  { path: 'account', component: AccountComponent },
  { path: 'signup', component: SignupComponent },
  /*  PÁGINAS  */
  { path: 'purchases', component: PurchaseRequestComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
