/* Register */
function showKey(){
	$("input[name='key']").removeAttr("disabled");
	$("label[for='id_key']").css({'display': 'block'});
	$("input[name='key']").css({'display': 'block'});
	$("input[name='key']").attr("required","required");
}
function hideKey(){
	$("input[name='key']").removeAttr("required");
	$("input[name='key']").attr("disabled", "disabled");
	$("label[for='id_key']").css({'display': 'none'});
	$("input[name='key']").css({'display': 'none'});
}
$("select[name='group']").change(function(){
	if($(this).val() != "general"){
		showKey();
	}else{
		hideKey();
	}
});



var search_values = [];

$(function(){
	$.get("/api/topics_titles/?format=json", function(data){
		var topics = data;
		for(var i=0 ; i< topics.length; i++){
			search_values.push(topics[i].title);
		}
	});
	$.get("/api/items_titles/?format=json", function(data){
		var items = data;
		for(var i=0 ; i< items.length; i++){
			search_values.push(items[i].title);
		}
	});
});

$("#search").autocomplete({
	source: search_values
});



$(function(){
	$("#list_topics_sort").sortable();
	$("#list_items_sort").sortable();
});
