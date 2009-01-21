bda = function() {};
bda.Cloud = function() {};

/* TODO: GENERIC!!! put this function somewhere else */
bda.Cloud.prototype.getQueryFromUrl = function(url) {
	/* Construct a jQuery conform query from any url with query params
	 * Example:
	 *   var query = getQueryFromUrl('http://xyz.com/?var_a=test&var_b=123');
	 * Value of query:
	 *   query == {'var_a':'test', 'var_b':'123'}
	 * And:
	 *   query.var_a == 'test'
	 */
	url = decodeURI(url);
	var query = {};
	var query_string = url.split('?')[1];
	if (query_string) {
		var query_items = query_string.split('&');
		if (query_items) {
			for(var i = 0; i< query_items.length; i++) {
				var item = query_items[i].split('=');
				if (item[1]) {
					query[item[0]] = item[1];
				}
			}
		}
	}
	return query;
}
var bdacloud = new bda.Cloud();

function bdaRebindCloud() {
	jQuery("#cloud a").unbind();
	jQuery("#cloud a").click(function(event){
		event.preventDefault();
		cornerstone_spinner.show("#cloud");
		var query = bdacloud.getQueryFromUrl(jQuery(this).attr('href'));
		jQuery("#cloud").load("@@bda.cloud.viewlet-body", query, bdaCloudCallback);
	});
}
function bdaCloudCallback() {
	bdaLoadContent();
	bdaRebindCloud();
}
function bdaLoadContent() {
	/* OVERWRITE THIS FUNCTION IN YOUR SPECIFIC IMPLEMENTATION (THEME) */
	cornerstone_spinner.show("#content div");
	jQuery("#content div").html(""); /* Default dummy behaviour */
}
jQuery(document).ready(function(){
	bdaRebindCloud();
});