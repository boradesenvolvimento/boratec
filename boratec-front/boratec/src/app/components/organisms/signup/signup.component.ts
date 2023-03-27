import { Component } from '@angular/core';

import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service'; 

import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { faLock } from '@fortawesome/free-solid-svg-icons';
import { ToastrService } from 'ngx-toastr'; 

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {
  emailIcon = faEnvelope;
  userIcon = faUser;
  passwordIcon = faLock;

  error: any;

  constructor(
    private authService: AuthService,
    private router: Router,
    private toastrService: ToastrService
  ) {}

  ngOnInit(): void {
  }
  showError() {
    this.toastrService.error('Erro no cadastro do usuário')
  }
  signup(name: string, email: string, phone: string, password: string, confirm_password: string){
    // Retirar primeiro nome e sobrenome
    let complete_name = name.split(' ');
    let first_name = complete_name[0];
    let last_name = complete_name.slice(1, complete_name.length).join(" ")

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();
    var admission_date = `${yyyy}-${mm}-${dd}`;

    if (password == confirm_password){
      this.authService.signup(
        email,
        password,
        admission_date,
        first_name,
        last_name,
        phone.replace(/[^\d]+/g,'')
      ).subscribe(
        {
          next: (success) => {
            this.login(email, password)
            },
          error: (error) => {
            this.error = error,
            console.log(error),
            this.showError()
          },
        }
      )
    }

  }

  login(email: string, password: string){
    this.authService.login(email, password).subscribe(
      {
        next: (success) => this.router.navigate(['purchases']),
        error: (error) => this.error = error,
      }
    );
  }
}
