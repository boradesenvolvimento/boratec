import { Component, OnInit } from '@angular/core';

import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service'; 

import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit{
  emailIcon = faEnvelope;

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

  login(username: string, password: string){
    this.authService.login(username, password).subscribe(
      {
        next: (success) => this.router.navigate(['purchases']),
        error: (error) => {
          this.error = error,
          console.log(error),
          this.showError()
        },
      }
    );
  }
}
