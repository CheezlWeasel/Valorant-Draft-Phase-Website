var text = [
  {
  Name: 'testfsagge',
  host: 'testermatter',
  map: 'HBO1',
  angent_draft: 'True'
}, {
  Name: 'testafwggge',
  host: 'testermatter',
  map: 'HBO1',
  angent_draft: 'True'
}, {
  Name: 'test324agge',
  host: 'testermatter',
  map: 'HBO1',
  angent_draft: 'True'
}, {
  Name: 'testkmutagge',
  host: 'testermatter',
  map: 'HBO1',
  angent_draft: 'True'
}]
for (var i in text) {
    var lobby = document.createElement("div");
    lobby.id = text[i].Name;
    lobby.className = "lobby";
    document.getElementById("actuallobbyarea").appendChild(lobby);
    var title = document.createElement("div");
    title.className = "lobby-title";
    title.innerHTML = text[i].Name;
    document.getElementById(text[i].Name).appendChild(title);
    var host = document.createElement("div");
    host.className = "host-name"
    host.innerHTML = text[i].host
    document.getElementById(text[i].Name).appendChild(host);
    };
        
    