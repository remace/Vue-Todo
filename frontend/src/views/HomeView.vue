<template>
  <main>
    <h1>Todo list</h1>
    <ul v-if="get_data">
      <li v-for="todo in todos" :key="todo.id">
        <TodoComponent 
          :title=todo.title 
          :description=todo.description
          :visible = todo.visible
          :done = todo.done
          :id = todo.id
          @delete="delete_todo"
        />
      </li>
    </ul>
    <div v-else>loading...</div>
    <input placeholder="title" ref="title_field">
    <input placeholder="description" ref="description_field">
    <button @click="addTodo">Ajouter</button>
  </main>
</template>

<script>
  import axios from 'axios'
  import TodoComponent from '../components/TodoComponent.vue'
  export default{
    data(){
      return{
        get_data: false,
        todos:[
          {}
        ]
      }
    },

    methods: {

      get_todos(){
        axios.get('http://127.0.0.1:5000/api/todos/')
        .then((res)=>{
          this.todos = res.data
          this.get_data = true
        })
        .catch((error)=>{
          console.log(error)
        })
      },


      addTodo(){

        let todo = {
          title: this.$refs.title_field.value ,
          description: this.$refs.description_field.value,
          done:false,
          visible:true
        }

        axios.post('http://127.0.0.1:5000/api/todo/create/',todo)
          .then((res)=>{
            console.log(res.data)
            this.todos.push(res.data)
          })
          .catch((error)=>{
            console.log(error)
          })
      },


      delete_todo(id){
        axios.delete(`http://127.0.0.1:5000/api/todo/${id}/`)
          .then((res)=>{
            console.log(res.data)
            let newTodos = this.todos.filter(todo => todo.id != res.data.id)
            this.todos = newTodos
          })
      }
    },

    mounted() {
      this.get_todos()
    },
    components: {
      TodoComponent,
    }  
  }

</script>

<style>
</style>