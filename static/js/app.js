// class for handling updating and deleting bugs from the frontend
class Bugs {
	constructor() {
		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
		axios.defaults.withCredentials = true;
	}
	UpdateBug(id, title, description, priority) {
		axios({
			method: 'put',
			url: '/bugs/' + id,
			data: {
				title: title,
				description: description,
				priority: priority
			}
		}).then(function(response) {
			console.log(response);
			location.reload();
		});
    }
    MarkAsFixed(id, status) {
        console.log();
        axios({
			method: 'put',
            url: '/bugs/' + id,
            data: {
                fixed: !(status)
            }
		}).then(function(response) {
			location.reload();
		});
    }

	DeleteBug(id) {
		axios({
			method: 'delete',
			url: '/bugs/' + id
		}).then(function(response) {
			window.location.href='/';
		});
	}
}

class Comments{
	constructor() {
		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
		axios.defaults.withCredentials = true;
	}
	ScoreComment(id, vote){
		console.log('voted', id, vote)
	}
	ScoreBug(id, vote) {
		console.log('voted', id, vote)
	}
}

bugs = new Bugs();
comments = new Comments();