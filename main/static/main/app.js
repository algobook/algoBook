var app = new Vue({
	el: '#app',
	delimiters: ['{!', '!}'],
	data: {
		query: window.location.pathname.replace("/","").replace("/",""),
		data: "",
		searching: 0,
		results: []
	},
	methods: {
		createAlgo: function(){
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
			var that = this
			$.get('../algos/search/'+ this.query.replace(" ", "+") , function(response){
				that.results = response.results
				console.log(that.results)
			})

		}
	}
})


Vue.component('algo', {})
