
<script lang="ts" setup>
import { useRoute } from 'vue-router';
import API from '../axios'

const route=useRoute()
let text= route.params.url

API.post('/select').then(
    function (response) {
    console.log(response);
  })

</script>

<template>
    <h1>{{text}}</h1>
</template>
