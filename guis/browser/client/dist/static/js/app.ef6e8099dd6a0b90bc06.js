webpackJsonp([1],{NHnr:function(o,n,t){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var e=t("7+uW"),a={name:"App",created:function(){console.log(this.$route)}},l={render:function(){var o=this.$createElement,n=this._self._c||o;return n("div",{attrs:{id:"app"}},[n("h1",[this._v(this._s(this.$route.meta.title))]),this._v(" "),n("router-view")],1)},staticRenderFns:[]};var r=t("VU/8")(a,l,!1,function(o){t("jedf")},null,null).exports,i=t("/ocq"),s=t("BO1k"),u=t.n(s),c=t("mtWM"),d=t.n(c),p=t("Zrlr"),f=t.n(p),m=function o(){f()(this,o)};m.host="";var b=m,h=t("M4fF");console.log("LODASH",h);var w={name:"my-component",data:function(){return{columns:[{label:"TagName",field:"TagName"},{label:"Time of last edition",field:"TimeEdt",formatFn:function(o){return new Date(1e3*o).toLocaleString()},type:"number"},{label:"Text",field:"Text"},{label:"BookTitle",field:"BookTitle",filterOptions:{enabled:!0,placeholder:"Filter This Thing",filterValue:"",filterDropdownItems:[],trigger:"enter"}},{label:"Actions",field:"actions"}],rows:[],booksFilter:[]}},created:function(){var o=this;d.a.get(b.host+"/api/annotations?tag=bm.quotation",{params:this.$route.query}).then(function(n){o.rows=n.data}),d.a.get(b.host+"/api/books").then(function(n){var t=[],e=!0,a=!1,l=void 0;try{for(var r,i=u()(n.data);!(e=(r=i.next()).done);e=!0){var s=r.value;t.push(s.Title)}}catch(o){a=!0,l=o}finally{try{!e&&i.return&&i.return()}finally{if(a)throw l}}o.columns.filter(function(o){return"BookTitle"===o.field})[0].filterOptions.filterDropdownItems=t})},methods:{handleOpenBook:function(o){d.a.post(b.host+"/api/open_annotation",{OID:o.OID})}}},g={render:function(){var o=this,n=o.$createElement,t=o._self._c||n;return t("div",[o.$route.query.bookId?t("h5",[o._v("For book "+o._s(o.$route.query.bookId))]):o._e(),o._v(" "),t("vue-good-table",{attrs:{columns:o.columns,rows:o.rows,"sort-options":{initialSortBy:{field:"TimeEdt",type:"desc"}},"pagination-options":{enabled:!0,mode:"records",perPage:50,position:"top",perPageDropdown:[3,7,9],dropdownAllowAll:!1,setCurrentPage:1,nextLabel:"next",prevLabel:"prev",rowsPerPageLabel:"Rows per page",ofLabel:"of",pageLabel:"page",allLabel:"All"}},scopedSlots:o._u([{key:"table-row",fn:function(n){return["actions"==n.column.field?t("span",[t("button",{on:{click:function(t){return o.handleOpenBook(n.row)}}},[o._v("Open book")])]):t("span",[o._v("\n          "+o._s(n.formattedRow[n.column.field])+"\n        ")])]}}])})],1)},staticRenderFns:[]},v=t("VU/8")(w,g,!1,null,null,null).exports,k={name:"my-component",data:function(){return{columns:[{label:"OID",field:"OID",type:"number"},{label:"Title",field:"Title"},{label:"Authors",field:"Authors"},{label:"Annotations Count",field:"AnnotationsCount",type:"number"},{label:"Actions",field:"actions"}],rows:[]}},created:function(){var o=this;d.a.get(b.host+"/api/books").then(function(n){console.log(n.data),o.rows=n.data})},methods:{handleButtonAnnotations:function(o){console.log("Annotations clicked!",o.row),this.$router.push({name:"annotations",query:{bookId:o.row.OID}})},handleDownloadAnnotations:function(o){window.location=b.host+"/markdown/annotations?bookId="+o.OID+"&tag=bm.quotation"}}},_={render:function(){var o=this,n=o.$createElement,t=o._self._c||n;return t("div",[t("vue-good-table",{attrs:{columns:o.columns,rows:o.rows,"pagination-options":{enabled:!0,mode:"records",perPage:50,position:"top",perPageDropdown:[3,7,9],dropdownAllowAll:!1,setCurrentPage:1,nextLabel:"next",prevLabel:"prev",rowsPerPageLabel:"Rows per page",ofLabel:"of",pageLabel:"page",allLabel:"All"}},scopedSlots:o._u([{key:"table-row",fn:function(n){return["actions"==n.column.field?t("span",[t("button",{on:{click:function(t){return o.handleButtonAnnotations(n)}}},[o._v("Annotations")]),o._v(" "),t("button",{on:{click:function(t){return o.handleDownloadAnnotations(n.row)}}},[o._v("Download annotations as Markdown")])]):t("span",[o._v("\n          "+o._s(n.formattedRow[n.column.field])+"\n        ")])]}}])})],1)},staticRenderFns:[]},A=t("VU/8")(k,_,!1,null,null,null).exports;e.a.use(i.a);var y=new i.a({routes:[{path:"/",name:"books",component:A,meta:{title:"Books"}},{path:"/annotations",name:"annotations",component:v,meta:{title:"Annotations"}}]}),T=t("sttX");t("gfot");e.a.config.productionTip=!1,e.a.use(T.a),new e.a({el:"#app",router:y,components:{App:r},template:"<App/>"})},gfot:function(o,n){},jedf:function(o,n){}},["NHnr"]);
//# sourceMappingURL=app.ef6e8099dd6a0b90bc06.js.map