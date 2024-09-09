from collections import deque;
import re;

from bs4 import BeautifulSoup;
import requests;
import urllib.parse;

user_url = str(inut('[+] Masukkan url: '));
urls = deque([user_url]);
scraped_urls = set();
emails = set();
count = 0;
limit = int(input('[+] Masukkan limit pencarian: '));

try:
	while True:
		count += 1;
		if count > limit:
			break;

		url = urls.popleft();
		scraped_urls.add(url);
		parts = urllib.parse.urlsplit(url);
		base_url = f'{parts.scheme}://{parts.netlock}';
		path = url[:url.rfind('/')+1] if '/' in parts.path else url

		print(f'{count} Memproses {url}');

		try:
			response = requests.get(url);
		except(reaquests.exceptions.MissingSchema, requests.exceptions.ConnectingError):
			continue;

		new_email = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+a-z\.]+', response.test, re.I));
		emails.update(new_emails);

		soup = BeautifulSoup(response.text, 'html.parse');
		for anchor in soup.find_all('a'):
			link = anchor.attrs['href'] if 'href' in anchor.attr else '';
			if link.startswith('/'):
				link = base_url + link;
			elif not link.startswith('http'):
				link = path + link;

			if not link in urls and not link in scraped_urls:
				urls.append(link);
except KeyboardInterrup:
	print('[-] Cloasing!');

print('\n Proses Selesai!');
print(f'\n{len(emails)} email ditemukan \n ==================================');

for mail in emails:
	print('    '+email);
print('\n');
