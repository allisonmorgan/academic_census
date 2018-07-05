
import networkx as nx
import requests
import matplotlib.pyplot as plt
import urlparse
import time

from bs4 import BeautifulSoup

def crawl_once(web_address):
	try:
		# Do a GET request on the URL provided
		r = requests.get(web_address, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'}) 
	except requests.exceptions.ConnectionError:
		print 'Invalid URL: {address}'.format(address=web_address)
		return 
	
	soup = BeautifulSoup(r.text, 'html.parser')
	
	# Parse response body to get all hyperlinks
	links = soup.find_all('a')
	keyword_dict = {}
	for link in links:
			url = link.get('href')
			if (type(url) is str) or (type(url) is unicode):
				url = urlparse.urljoin(web_address, url)
				text = link.string

				if not keyword_dict.has_key(url):
					keyword_dict[url] = []

				if type(text) != type(None):
					keyword_dict[url].append(text.lower())

	return keyword_dict

def build_graph(g, url, domain, n_hops = 3, n_iter = 0):
	# If n_iter == n_hops, then return
	if n_iter == n_hops:
		return g

	# Start at the url given and go one hop out
	links_and_keywords = crawl_once(url)
	links_queue = set([key for key, _ in links_and_keywords.items()])
	for outgoing in links_queue:
		if outgoing.count('mailto') > 0 or str(outgoing).count(str(domain)) == 0:
			# print(outgoing, n_iter)
			continue

		# print(outgoing, n_iter)
		g.add_edge(url, outgoing)

		# Now, look at all links outgoing from 'outgoing'
		time.sleep(0.01)
		g = build_graph(g, outgoing, domain, n_hops, n_iter+1)

	return g

if __name__ == '__main__':

	g = build_graph(nx.Graph(), 'http://www.cs.ucdavis.edu', 'cs.ucdavis.edu', n_hops = 2)

	labels = {
		u'http://www.cs.ucdavis.edu': u'http://www.cs.ucdavis.edu', 
		u'http://www.cs.ucdavis.edu/people/faculty/': u'http://www.cs.ucdavis.edu/people/faculty/'
	}

	# Assign a node attribute
	for node in g.nodes():
		if node in labels.keys():
		    g.node[node]['color'] = 'orange'
		else:
			g.node[node]['color'] = 'gray'
	# Put together a color map, one color for a category
	color_map = {'orange':'#e66101', 'gray':'#D3D3D3'} 

	plt.figure(figsize=(6,4))
	pos = nx.spring_layout(g)
	nx.draw_networkx_nodes(g, pos, node_color=[color_map[g.node[node]['color']] for node in g], alpha=0.5, linewidths=0.25)
	nx.draw_networkx_edges(g, pos, alpha=0.025, edge_color='k')
	nx.draw_networkx_labels(g, pos=pos, labels=labels)
	plt.axis('off')
	plt.savefig('davis.png', bbox_inches='tight')
	plt.clf()

	# Save GML file
	nx.write_gml(g, 'davis.gml')


