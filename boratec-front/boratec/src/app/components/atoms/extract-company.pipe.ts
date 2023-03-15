import { Pipe, PipeTransform } from '@angular/core';
import { environment } from 'src/environments/environment';

@Pipe({
  name: 'extractCompany'
})
export class ExtractCompanyPipe implements PipeTransform {
  // type var | 'C' para company ou 'B' para branch
  transform(company: string, branch: string, type: string ): string {
    if (type.toUpperCase() == 'C'){
      return String(environment.company[company]);
    } else if (type.toUpperCase() == 'B') {
      return String(environment.branches[company][branch]);
    } else {
      return `Não foi possível encontar a filial ${company} - ${branch}`
    }
  }

}
