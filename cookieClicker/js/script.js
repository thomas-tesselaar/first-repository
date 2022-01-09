currScore = 0;
booster =1;

function ruleson() {
  document.getElementById('rulestitle').innerHTML = "Rules \\/";
  document.getElementById('rulebook').style.display = "block";
}

function rulesoff() {
  document.getElementById('rulestitle').innerHTML = "Rules >";
  document.getElementById('rulebook').style.display = "none";
}

function cookieClick() {
  currScore += booster;
  document.getElementById('score').innerHTML = currScore;

  if(currScore >= 10000) {
    document.getElementById('score').innerHTML = "Good job, you won";
  }
}

function boosterClick() {
  if (currScore >= 10) {
    currScore -= 10;
    booster += 1;
    document.getElementById('score').innerHTML = currScore;
    document.getElementById('warning').style.display = "none";
    document.getElementById('boosted').style.display = "block";
    document.getElementById('boosted').innerHTML = "Clicker boosted! Booster is now " + booster;
  } else {
    document.getElementById('warning').style.display = "block";
  }
}

function reset() {
  currScore = 0;
  booster = 1;
  document.getElementById('score').innerHTML = currScore;
  document.getElementById('warning').style.display = "none";
  document.getElementById('boosted').style.display = "none";
}
