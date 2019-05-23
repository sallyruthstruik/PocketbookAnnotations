<template>
  <div>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :pagination-options="{
        enabled: true,
        mode: 'records',
        perPage: 50,
        position: 'top',
        perPageDropdown: [3, 7, 9],
        dropdownAllowAll: false,
        setCurrentPage: 1,
        nextLabel: 'next',
        prevLabel: 'prev',
        rowsPerPageLabel: 'Rows per page',
        ofLabel: 'of',
        pageLabel: 'page', // for 'pages' mode
        allLabel: 'All',
      }">
        <template slot="table-row" slot-scope="props">
          <span v-if="props.column.field == 'actions'">
            <button v-on:click="handleButtonAnnotations(props)">Annotations</button>
            <button v-on:click="handleDownloadAnnotations(props.row)">Download annotations as Markdown</button>
          </span>
          <span v-else>
            {{props.formattedRow[props.column.field]}}
          </span>
        </template>
    </vue-good-table>
  </div>
</template>

<script>
import axios from "axios"
import Config from "../config.js"
export default {
  name: 'my-component',
  data(){
    return {
      columns: [
        {
          label: 'OID',
          field: 'OID',
          type: 'number',
        },
        {
          label: 'Title',
          field: 'Title',
        },{
          label: 'Authors',
          field: 'Authors',
        },{
          label: 'Annotations Count',
          field: 'AnnotationsCount',
          type: 'number',
        }, {
          label: 'Actions',
          field: 'actions',
        },
      ],
      rows: [

      ],
    };
  },

  created(){
    axios.get(`${Config.host}/api/books`)
      .then(response=>{
        console.log(response.data);
        this.rows = response.data;
      })
  },

  methods: {
    handleButtonAnnotations(item){
      console.log("Annotations clicked!", item.row);
      this.$router.push({name: "annotations", query: {bookId: item.row.OID}})
    },

    handleDownloadAnnotations(row){
      window.location = `${Config.host}/markdown/annotations?bookId=${row.OID}&tag=bm.quotation`
    },
  },

};
</script>
