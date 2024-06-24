import { Permissions } from './permissions';

export class Menu {
  private permissions = new Permissions();

  public async menuGenrator(hideMenus: boolean) {
    let menus;
    menus = [
      {
        name: 'Todo App',
        visible: this.permissions.isGranted('Pages.AppStudio.TodoApp.Read'),
        icon: '',
        selected: 'Todo App',
        isCollapsed: true,
        route: {
          url: ['/too-app']
        }
      }
    ];
    return menus;
  }
}
