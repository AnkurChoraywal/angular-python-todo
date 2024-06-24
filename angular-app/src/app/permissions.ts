export class Permissions {
    /**
     * Public Method isGranted
     * input will be Permission Key like Tickets.Create
     * Logic: check if permission exist or isSuperUser == true
     * uses: Import this method and check in auth-guard, html and componant
     */
    public isGranted(input: string) {
      let user = JSON.parse(localStorage.getItem('user') || '{}');
      if (
        user?.permissions?.filter((p: { permissionName: string }) => p.permissionName === input).length > 0 ||
        user?.isSuperuser
      ) {
        return true;
      } else {
        return false;
      }
    }
    public isRestricted() {
      let user = JSON.parse(localStorage.getItem('user') || '{}');
      if (!user?.isSuperuser && user?.permissions?.length == 0) {
        return false;
      } else {
        return true;
      }
    }
  }
  