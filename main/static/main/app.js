var app = new Vue({
	el: '#app',
	delimiters: ['{!', '!}'],
	data: {
		query: window.location.pathname.replace("/","").replace("/",""),
		data: "",
		searching: 0,
		results: [],
		createError: false,
		keepit: 1,
		notfound: 0
	},
	methods: {
		createAlgo: function(){
			this.createError = false;

			if (!this.query.length)
			{
				this.createError = true;
				return 0;
			}

			var form = document.createElement("form")
			form.method = "POST"
			form.action = "../../algos/create"

			var input = document.createElement("input")
			input.type="text"
			input.name="name"
			input.value = this.query

			csrf = $("#csrf").children()[0]

			form.appendChild(input)
			form.appendChild(csrf)
			form.submit();
		},

		getData: function(){
			// TODO: set csrf token here

			this.searching  = 1
			this.notfound = 0
			this.results = []
			var that = this
			$.get('../algos/search/'+ this.query.replace(" ", "+") , function(response){
				that.results = response.results
				that.keepit = false
				that.searching= 0
			}).fail(function(){
				that.notfound = 1
			})

		}
	}
})


Vue.component('algo', {})
