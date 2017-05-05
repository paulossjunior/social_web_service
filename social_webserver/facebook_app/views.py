
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib.request
import json
import facebook

class Facebook_User(APIView):

    def get(self, request, pk, format=None):

        social_user = request.user.social_auth.filter(provider='facebook', ).first()

        if social_user:

            access_token = social_user.extra_data['access_token']



            #url = "https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cbirthday%2Clink%2Cfriends%7Bid%2Cname%7D&access_token=" + access_token
            #url = "https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cbirthday%2Ceducation%2Clink&access_token=" + access_token
            url = "https://graph.facebook.com/v2.9/me?fields=friends%7Bid%2Cname%7D&access_token=" + access_token

            request = urllib.Request(url)
            friends = json.loads(urllib.urlopen(request).read()).get('data')
            for friend in friends:
                name = friend.get('name')
                print (name)


            return Response(friends)

        return Response('Xiii')


