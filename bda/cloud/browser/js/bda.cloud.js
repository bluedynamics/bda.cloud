bda = function() {};
bda.Cloud = function(cloud_selector, content_selector, content_url,
					 /* optional */ content_query) {
    this.cloud_selector = cloud_selector;
	this.content_selector = content_selector;
	this.content_url = content_url;
	if (!content_query) content_query = {};
	this.content_query = content_query;
};

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
bda.Cloud.prototype.rebindCloud = function() {
	var bdac = this;
    jQuery(bdac.cloud_selector + " a").unbind();
	jQuery(bdac.cloud_selector + " a").click(function(event){
		event.preventDefault();
		cornerstone_spinner.show(bdac.cloud_selector);
		var query = bdac.getQueryFromUrl(jQuery(this).attr('href'));
		/* jQuery(bdac.cloud_selector).load("@@bda.cloud.viewlet-body", query,
						                     bdac.cloudCallback);
			when calling bdac.cloudCallback, bdac.cloudCallback has no access
			to bdac variable anymore.
			with following inner function it has.
			there may be another solution when using closures or that stuff.
		*/
		jQuery(bdac.cloud_selector).load("@@bda.cloud.viewlet-body", query,
			function () {
				cornerstone_spinner.show(bdac.content_selector);
				jQuery(bdac.content_selector).load(bdac.content_url, bdac.content_query);
				bdac.rebindCloud();
			}
		);
	});
}

/* INITIALIZE IN YOUR SPECIFIC IMPLEMENTATION LIKE SO: */
/* It should be possible to instantiate more than one cloud */
/*
jQuery(document).ready(function(){
	var bdacloud = new bda.Cloud(
		'#cloud', // CLOUDSELECTOR
		'#content', // CONTENTSELECTOR
		'@@blogkssview', // CONTENT SCHNIPSEL URL
		{} // ADDITIONAL CONTENT URL QUERY PARAMETER
	);
	bdacloud.rebindCloud();
});
*/