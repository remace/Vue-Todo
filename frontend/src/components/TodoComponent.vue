<template>
<div class=wrapper>
    <div class="todo-title">{{title}}</div>
    <div class="todo-description">{{ description }}</div>
    <div class="todo-done">done: {{ done }}</div>
    <div class="todo-visible">visible: {{ visible }}</div>
    <button @click="delete_todo">delete todo</button>
</div>

</template>

<script>
    export default{
        props:{
            title:String,
            description:String,
            visible:Boolean,
            done:Boolean,
            id:Number,
        },
        methods:{
            delete_todo(){
                console.log(`composant TODO - id: ${this.id}`)
                this.$emit('delete', `${this.id}`)
            }
        },
        emits:['delete']


    }
</script>

<style scoped>
.wrapper{
    display:flex;
    justify-content: space-between;
}

</style>