// GENERIC!!! put this function somewhere else
function getQueryFromUrl(url) {
	// construct a jQuery conform url from any url with query params
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

// GENERIC!!! put this function somewhere else
function bdaSpinner(content_id) {
	jQuery(content_id).html(jQuery("#kss-spinner").html());
	jQuery(content_id + ' img').css({
		"display":"block",
		"margin-top":"20px",
		"margin-bottom":"20px",
		"margin-left":"auto",
		"margin-right":"auto"
	});
}

function bdaRebindCloud() {

	/*jQuery("#cloud").unbind();
	jQuery("#cloud").ajaxComplete(function(request, settings){
		// THIS ONE DOES NOT WORK.
		// ajaxComplete event seems to be fired continiously
	});*/

	jQuery("#cloud a").unbind();
	jQuery("#cloud a").click(function(event){
		event.preventDefault();
		bdaSpinner("#cloud");
		var query = getQueryFromUrl(jQuery(this).attr('href'));
		jQuery("#cloud").load("@@bda.cloud.viewlet-body", query, bdaCloudCallback);
	});
}

function bdaCloudCallback() {
	bdaLoadContent();
	bdaRebindCloud();
}
function bdaLoadContent() {
	/* OVERWRITE THIS FUNCTION IN YOUR SPECIFIC IMPLEMENTATION (THEME) */
	bdaSpinner("#content div");
	jQuery("#content div").html(""); /* Default dummy behaviour */
}

jQuery(document).ready(function(){
	bdaRebindCloud();
});