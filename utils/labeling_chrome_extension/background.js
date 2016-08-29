var query_array;
var query_index = 0;
var result = '';
var boundary_index;

// Listener of message port to 'content.js'
chrome.runtime.onConnect.addListener(function(port) { 
  port.onMessage.addListener(function(msg) {
    console.log("경계면을 " + (Number(msg)+1) + "번째 이미지로 지정하셨습니다");
    boundary_index = msg;
  });
});

// BrowserAction(when click icon)
chrome.browserAction.onClicked.addListener(function(tab) {
  console.log(chrome.extension.getURL('query.txt'));
  function readQueryList() {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
      query_array = xhr.responseText.split('\n');
      setTimeout(readQueryList, 5000);
    };
    xhr.open('GET', chrome.extension.getURL('query.txt'), false);
    xhr.send();
  }
  readQueryList();
  if (result != '') {
    uri = 'data:application/octet-stream,' + encodeURIComponent(result);
    window.open(uri, 'result.txt');
  }
  console.log(query_array);
  console.log("총 " + query_array.length + " 페이지를 진행해야 합니다");

  var newurl = 'http://google.co.kr/search?q=' + query_array[query_index] + '&tbm=isch'
  chrome.tabs.create({url: encodeURI(newurl)});
});

// Command(Keyboard Shortcut) Listener
chrome.commands.onCommand.addListener(function(command) {
  // Get the currently selected tab
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var tab = tabs[0];
    result = result + query_array[query_index] + ';' + boundary_index + '\n';
    query_index += 1;
    if (query_index % 50 === 0) {
      uri = 'data:application/octet-stream,' + encodeURIComponent(result);
      window.open(uri, 'result.txt');
    }
    console.log(result);
    console.log("현재까지 " + query_index + "/" + query_array.length + " 진행중입니다");
    if (query_index+1 >= query_array.length) {
      alert("해당 패턴에 대한 라벨링이 끝났습니다")
      uri = 'data:application/octet-stream,' + encodeURIComponent(result);
      window.open(uri, 'result.txt');
    }
    var newurl = 'http://google.co.kr/search?q=' + query_array[query_index] + '&tbm=isch'
    chrome.tabs.update(tab.id, {url: encodeURI(newurl)});
  });
});
