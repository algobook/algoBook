

var app = new Vue({
	el: '#app',
	delimiters: ['((', '))'],
	data: {
		query: $("#squery").html(),
		data: "",
		searching: 0,
		results: [],
		createError: false,
		keepit: 1,
		notfound: 0,
		showResults: 0
	},
	methods: {

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

			var form = $("form")[0]
			form.method = "GET"
			form.action = "../../algos/create"

			var input = $("input")[0]
			input.type="text"
			input.name="name"
			input.value = this.query

			csrf = $("#csrf").children()[0]

			form.appendChild(input)

			form.submit();
		},

		getData: function(){
			// TODO: set csrf token here
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
			return "../algo/" + uri;
		}
	}
})


Vue.component('algo', {})
