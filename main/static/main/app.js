var app = new Vue({
	el: '#app',
	data: {
		query: "",
		data: ""
	},
	methods: {
		highlightBlock: function(){
			$('pre code').each(function(i, block) {
			    hljs.highlightBlock(block);
			});
		}
	}
})


Vue.component('algo', {})
