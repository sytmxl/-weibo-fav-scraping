# scraping
go to fav page(https://weibo.com/u/page/fav/3915117809) and check network for the request of fav infos.
tell llm how to request and get script.
fill cookies in script.(cookies can be found in detailed info of request).
script design:
Fetch total number of favorites first.
get favorites according to total number.
save item in ./favorites/favorites_page_{n}.json
# display
# management