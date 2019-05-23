<template>
  <div>
    <h5 v-if="$route.query.bookId">For book {{$route.query.bookId}}</h5>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :sort-options="{
        initialSortBy: {field: 'TimeEdt', type: 'desc'},
      }"
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
            <button v-on:click="handleOpenBook(props.row)">Open book</button>
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
const lodash  = require("lodash");
console.log("LODASH", lodash);

export default {
  name: 'my-component',
  data(){
    return {
      columns: [
        {
          label: 'TagName',
          field: 'TagName',
        },
        {
          label: 'Time of last edition',
          field: 'TimeEdt',
          formatFn: (val)=>{
            return new Date(val*1000).toLocaleString();
          },
          type: 'number',
        },
        {
          label: 'Text',
          field: 'Text',
        },{
          label: 'BookTitle',
          field: 'BookTitle',
          filterOptions: {
            enabled: true, // enable filter for this column
            placeholder: 'Filter This Thing', // placeholder for filter input
            filterValue: '', // initial populated value for this filter
            filterDropdownItems: [], // dropdown (with selected values) instead of text input
            trigger: 'enter', //only trigger on enter not on keyup
          },
        }, {
          label: "Actions",
          field: "actions",
        }
      ],
      rows: [

      ],
      booksFilter: [

      ],
    };
  },

  created(){
    axios.get(`${Config.host}/api/annotations?tag=bm.quotation`, {params: this.$route.query})
      .then(response=>{
        this.rows = response.data;
      });

    axios.get(`${Config.host}/api/books`)
      .then(response=>{
        let bookTitles = [];
        for (let book of response.data){
          bookTitles.push(book.Title)
        }
        this.columns.filter(v=>v.field === 'BookTitle')[0].filterOptions.filterDropdownItems = bookTitles;
      })
  },

  methods: {
    handleOpenBook(row){
      axios.post(`${Config.host}/api/open_annotation`, {OID: row.OID})
    },
  },
};
</script>
filterDropdownItems
