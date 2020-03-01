// class for handling updating and deleting bugs from the frontend
class Bugs {
	constructor() {
		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
		axios.defaults.withCredentials = true;
	}
	UpdateBug(id) {
		axios({
			method: 'put',
			url: '/bugs/' + id
		}).then(function(response) {
			console.log(response);
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

bugs = new Bugs();
