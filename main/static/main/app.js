

var app = new Vue({
	el: '#app',
	delimiters: ['((', '))'],
	data: {
		query: function(){
			return $('#squery').html()
		}(),
		data: "",
		searching: 0,
		results: [],
		createError: false,
		keepit: 1,
		notfound: 0,
		showResults: 0
	},
	methods: {

		getLang : function(query){
	        query = query.replace("/ /g","+")
	        var pos = query.lastIndexOf(" in ")
	        if( pos != -1)
	            return query.substr(pos+4)
	        else
	            return ""
	    },
	    getQuery : function(query){
	        query = query.replace("/ /g","+")
	        var pos = query.lastIndexOf(" in ")
	        if( pos != -1)
            	return query.substr(0,pos)
	        else
	            return query
	    },
		onload: function(){

		},

		isThere: function(val){
			if(val == "")
				return "none"
			else
				return val
		},
		
		createAlgo: function(){
			this.createError = false;
			if (!this.query.length)
			{
				this.createError = true;
				return 0;
			}

			location = "../../algos/create?lang=" + this.getLang(this.query) + "&name=" + this.getQuery(this.query)

			// var form = $("form")[0]
			// form.method = "GET"
			// form.action = "../../algos/create"

			// var input = $("input")[0]
			// input.type="text"
			// input.name="lang"
			// input.value = this.getLang(this.query)

			// var input = $("input")[0]
			// input.type="text"
			// input.name="name"
			// input.value = 

			// csrf = $("#csrf").children()[0]

			// form.appendChild(input)

			// form.submit();
		},

		getData: function(){
			// TODO: set csrf token here
			// alert(this.query)
			query = getSearchQuery( this.query )
			this.searching  = 1
			this.notfound = 0
			this.results = []
			this.showResults = 1
			var that = this
			$.get('../algos/search/'+ query , function(response){
				that.results = response.results
				that.showResults = 1
				that.keepit = false
				that.searching= 0
			}).fail(function(){
				that.notfound = 1
			})

		},
		urltoalgo: function(uri){
			return "../algo/" + uri + "?lang=" + this.getLang(this.query);
		}
	}
})


Vue.component('algo', {})
