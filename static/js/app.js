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
			location.reload();
		});
    }
    MarkAsFixed(id, status) {
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
	ScoreComment(bugId, commentId, vote){
		axios({
			method: 'put',
			url: `/bugs/${bugId}/comment`,
			data: {
				vote: vote,
				comment: commentId
			}
		}).then(function(response){
			location.reload();
			console.log('voted, reloaded', response)
		})
	}
	ScoreBug(bugId, vote) {

	}
}

bugs = new Bugs();
comments = new Comments();