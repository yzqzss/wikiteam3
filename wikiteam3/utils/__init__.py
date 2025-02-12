from .uprint import uprint
from .util import removeIP, cleanXML, cleanHTML, undoHTMLEntities, sha1File

from .user_agent import getUserAgent
from .domain import domain2prefix
from .wiki_avoid import avoidWikimediaProjects
from .monkey_patch import mod_requests_text
from .login import uniLogin, fetchLoginToken, botLogin, clientLogin, indexLogin