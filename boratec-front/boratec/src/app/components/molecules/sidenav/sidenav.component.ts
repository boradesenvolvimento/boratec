import { Component, OnInit } from '@angular/core';
import { faX } from '@fortawesome/free-solid-svg-icons';
import { faHouseChimney } from '@fortawesome/free-solid-svg-icons';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { faUserPlus } from '@fortawesome/free-solid-svg-icons';
import { faUserGear } from '@fortawesome/free-solid-svg-icons';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit{

  is_logged = false;
  collapsed: boolean = false;
  user_icon = faUser;
  user_register = faUserPlus;
  user_settings = faUserGear;
  close = faX;

  navPages = [
    {
      routeLink: 'purchases',
      icon: faHouseChimney,
      label: 'Início'
    }
  ]
  constructor(
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.is_logged = this.authService.isLoggedIn();
  }

  toggleCollapse(): void {
    this.collapsed = !this.collapsed;
  }

  closeSidenav(): void {
    this.collapsed = false
  }
}
