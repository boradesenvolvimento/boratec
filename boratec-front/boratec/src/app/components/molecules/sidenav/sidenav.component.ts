import { Component } from '@angular/core';
import { faX } from '@fortawesome/free-solid-svg-icons';
import { faHouseChimney } from '@fortawesome/free-solid-svg-icons';
import { faCircleUser } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent {

  collapsed: boolean = false;
  close = faX
  navPages = [
    {
      routeLink: 'account',
      icon: faCircleUser,
      label: 'Conta'
    },
    {
      routeLink: 'purchase',
      icon: faHouseChimney,
      label: 'Início'
    }
  ]
  toggleCollapse(): void {
    this.collapsed = !this.collapsed;
  }

  closeSidenav(): void {
    this.collapsed = false
  }
}
