import requests


def _url(path):
    return "https://help.ibureau.services/rest/" + path


def get_user(encoded_auth):
    return requests.get(_url("/auth/1/session"),
                        headers={'Authorization': encoded_auth})


def login_user(json_user):
    return requests.post(_url("/auth/1/session"),
                         json=json_user)


def logout_user(encoded_auth):
    return requests.delete(_url("/auth/1/session"),
                           headers={'Authorization': encoded_auth})


def search_issues(encoded_auth, username):
    jql = "assignee = " + username + " AND fixVersion not in (Future, FUTURE) AND status not in (Done, UAT, " \
                                     "Canceled, Closed, Resolved) ORDER BY priority DESC "
    json = {"jql": jql, "startAt": 0, "maxResults": 200}

    return requests.post(_url("/api/2/search"),
                         headers={'Authorization': encoded_auth},
                         json=json)
