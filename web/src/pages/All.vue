<script>
import axios from 'axios';

export default {
    data (){
        return{
            data: null,
            query: '',
            emptySearch: false,
            field: 'name',
        };
    },
    methods: {
        console() {
            console.log(this.query)
        },
        checkEmpty() {
            this.emptySearch = true;
            for (let i = 0; i < this.data.length; i++)
            {
                if (this.data[i][this.field].toLowerCase().includes(this.query.toLowerCase()))
                {
                    this.emptySearch = false;
                    return;
                }
            }
        }
    },
    watch: {
        query() {
            this.checkEmpty();
        },
        field() {
            this.checkEmpty();
        }
    },
    created() {
        axios
            .get('http://127.0.0.1:8000/load-all')
            .then((response) => {
                this.data = response.data;
            })
    }
}
</script>
<template>
  <h1 v-if="!data" class="loading-text">Loading...</h1>
  <div v-else class="w-screen text-sm font-thin text-slate-700">
    <div
      class="h-screen landscape:w-1/2 text-center overflow-y-auto m-auto p-2"
    >
      <!-- https://stackoverflow.com/questions/74367340/use-nth-childodd-css-selector-with-tailwind-on-the-parent-element -->
      <input
        v-model="query"
        class="border rounded my-2 w-full placeholder:text-center"
        placeholder="Search..."
      />
      <h3 v-if="emptySearch">Nothing to show.</h3>
      <table
        v-else
        class="dark:text-zinc-300 w-full m-auto [&>*:nth-child(odd)]:bg-gray-100 [&>*:nth-child(even)]:bg-gray-200 dark:[&>*:nth-child(odd)]:bg-slate-500 dark:[&>*:nth-child(even)]:bg-slate-600 shadow-sm"
      >
        <tr class="border dark:border-slate-700">
          <th class="p-2">
            <input type="radio" id="name" value="name" v-model="field" />
            Name
          </th>
          <th>
            <input type="radio" id="type" value="wtype" v-model="field" />
            Type
          </th>
          <th>
            <input type="radio" id="origin" value="region" v-model="field" />
            Origin
          </th>
        </tr>
        <tr
          v-for="item in data"
          class="border dark:border-slate-700 hover:opacity-70"
        >
          <template
            class="relative"
            v-if="item[field].toLowerCase().includes(query.toLowerCase())"
          >
            <router-link :to="`/${item.slug}`">
              <td
                class="p-1 text-blue-900 dark:text-zinc-100 hover:underline"
                v-text="item.name"
              ></td>
            </router-link>
            <td
              class="border dark:border-slate-700 p-1"
              v-text="item.wtype"
            ></td>
            <td class="p-1" v-text="item.region"></td>
          </template>
        </tr>
      </table>
    </div>
  </div>
</template>
