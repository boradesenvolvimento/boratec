import { Injectable } from '@angular/core';
import { HttpClient, HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';

import { Observable } from 'rxjs';
import { tap, shareReplay } from 'rxjs/operators';

import jwtDecode from 'jwt-decode';
import * as moment from 'moment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiRoot = 'http://127.0.0.1:8000/auth/';

  constructor(private http: HttpClient) { }

  private setSession(authResult) {
    if (authResult.error) {
      throw new Error('Email ou senha inválido')
    }
    const token = authResult;
    const payload = <JWTPayload> jwtDecode(token.access);
    const expiresAt = moment.unix(payload.exp);

    localStorage.setItem('token', authResult.access);
    if (authResult.refresh) {
      localStorage.setItem('refresh', authResult.refresh)
    }
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }

  get token(): string {
    return String(localStorage.getItem('token'));
  }

  get refresh(): string {
    return String(localStorage.getItem('refresh'));
  }

  login(username: string, password: string) {
    return this.http.post(
      this.apiRoot.concat('login/'),
      { 'email': username, 'password': password }
    ).pipe(
      tap(response => this.setSession(response)),
      shareReplay(),
    );
  }
  get_user(){
    return this.http.get(
      this.apiRoot.concat('login/')
    ).pipe(
      tap(response => console.log(response))
    )
  }

  signup(email: string, password: string, admission: string, first_name: string, last_name: string, phone: string) {
    // TODO: implement signup

    return this.http.post(
      this.apiRoot.concat('signup/'),
      {
        'email': email,
        'password': password,
        'admission': admission,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
      }
    ).pipe(
      tap(response => console.log(response))
    )
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('expires_at');
  }

  refreshToken() {
    if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
      return this.http.post(
        this.apiRoot.concat('jwt/refresh/'),
        { refresh: this.refresh }
      ).pipe(
        tap(response => this.setSession(response)),
        shareReplay(),
      ).subscribe();
    }
  }

  getExpiration() {

    const expiration = localStorage.getItem('expires_at');
    const expiresAt = JSON.parse(expiration || '{}');

    return moment(expiresAt);
  }

  isLoggedIn() {
    return moment().isBefore(this.getExpiration());
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }
}

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = localStorage.getItem('token');

    if (token) {
      const cloned = req.clone({
        headers: req.headers.set('Authorization', 'JWT '.concat(token))
      });

      return next.handle(cloned);
    } else {
      return next.handle(req);
    }
  }
}

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  canActivate() {
    if (this.authService.isLoggedIn()) {
      this.authService.refreshToken();

      return true;
    } else {
      this.authService.logout();
      this.router.navigate(['login']);

      return false;
    }
  }
}

interface JWTPayload {
  user_id: number;
  email: string;
  exp: number;
}