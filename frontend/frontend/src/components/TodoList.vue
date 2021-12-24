<template>
  <div class="container">
    <h1>TodoList</h1>
    <button class="btn btn-success">Add Todo</button>
    <table>
      <thead>
        <tr>
          <th>done</th>
          <th>title</th>
          <th>description</th>
          <th>created_at</th>
          <th>updated_at</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(todo, index) in todos" :key="index">
          <td v-if="todo.done"><i class="bi bi-check-square"></i></td>
          <td v-else><i class="bi bi-square"></i></td>
          <td>{{ todo.title }}</td>
          <td>{{ todo.description }}</td>
          <td>{{ BuildDate(todo.created_at) }}</td>
          <td>{{ BuildDate(todo.updated_at) }}</td>
          <td><button class="btn btn-primary">update</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "TodoList",
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    BuildDate(datetimeString) {
      let d = new Date(datetimeString);
      console.log(d);
      /*const months = [
        "Jan.",
        "Fév.",
        "Mars",
        "Avril.",
        "Mai",
        "Jun.",
        "Jui.",
        "Août",
        "Sept.",
        "Oct.",
        "Nov.",
        "Dec.",
      ];*/
      let days = [
        "Dim.",
        "Lun.",
        "Mar.",
        "Mer.",
        "Jeu.",
        "Ven.",
        "Sam.",
      ];

      const day = days[d.getDay()];
      const date = d.getDate();
      const month = d.getMonth() + 1;
      const year = d.getFullYear();
      const hour = d.getHours();
      const min = d.getMinutes();
      const sec = d.getSeconds();
      return `${day} ${date}/${month}/${year} ${hour}:${min}:${sec}`;
    },
    getTodos() {
      const myHeaders = new Headers();
      let payload = {
        method: "GET",
        headers: myHeaders,
        mode: "cors",
        cache: "default",
      };
      fetch("http://127.0.0.1:5000/api/todos/", payload)
        .then((res) => {
          return res.json();
        })
        .then((res) => {
          this.setTodos(res);
        });
    },
    setTodos(todos) {
      this.todos = todos;
    },
  },
  mounted() {
    this.getTodos();
  },
};
</script>

<style scoped></style>
