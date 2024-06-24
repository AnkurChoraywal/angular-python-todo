import { Component, ChangeDetectorRef, OnInit  } from '@angular/core';
import { HttpClient } from '@angular/common/http'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  data: any;
  hostUrl: string = 'http://localhost:8080'
  formData: any = {};
  todoList: any = [];

  constructor(private http: HttpClient, private cdRef: ChangeDetectorRef){}

  ngOnInit(){
    this.loadTodos()
  }

  loadTodos(){
    this.http.get(`${this.hostUrl}/todos`).subscribe(response => {
      this.todoList = response;
      this.cdRef.markForCheck();
    })
  }

  onSubmitNewTodo(form: any){
    this.http.post(`${this.hostUrl}/todos?title=${form.title}`, {}).subscribe(response => {
      this.loadTodos()
      this.formData.title = ''
    })
  }

  deleteTodo(id: number){
    this.http.delete(`${this.hostUrl}/todos/${id}`).subscribe(response => {
      this.loadTodos()
    })
  }

  onCheckboxChange(event: any, id: number){
    this.http.patch(`${this.hostUrl}/todos/${id}?completed=${event.target.checked}`, {}).subscribe(response => {
      this.loadTodos()
    })
  }

  
}
