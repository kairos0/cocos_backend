from django.conf import settings
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin

# class SessionRecordMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print("SessionRecordMiddleware")
#         # request.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get("REMOTE_ADDR"))
#         if request.user.is_authenticated:
#             session = request.session
#             session["user_agent"] = request.META.get("HTTP_USER_AGENT", "")
#             session["ip"] = request.ip
#             session["last_activity"] = now()
#             user_sessions = request.user.session_keys
#             if session.session_key not in user_sessions:
#                 user_sessions.append(session.session_key)
#                 request.user.save()