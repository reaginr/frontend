# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
import logging
from django.db.models import F


from home_application.models import ApiRequestCount

logger = logging.getLogger(__name__)

# 这里的CMDB和JOB对应的名称应该同你的URL定义的前缀，详见 /home_application/urls.py

CMDB_BEHAVIORS = [
    'biz-list',
    'set-list',
    'module-list',
    'host-list',
    'host-detail'
]

JOB_BEHAVIORS = [
    'search-file',
    'backup-file',
    'backup-record'
]


class RecordUserBehaviorMiddleware(MiddlewareMixin):
    """
    自定义中间件-记录用户行为，进行埋点
    """
    def process_request(self, request):
        try:
            # 获取需要埋点存储的信息：⽤户名、请求的API名称、请求的API所属的类别（CMDB/JOB）
            username = request.user.username
            # 可以观察⼀下这⾥的request.path 数据格式为 xxxx/xxxx/实际API名称，因此我们使⽤split⽅法，以 / 进⾏分割，只取最后的API名称部分
            api_name = request.path.split('/')[-1]
            # 判断接⼝所属类别
            api_category = 'CMDB' if api_name in CMDB_BEHAVIORS else 'JOB' if api_name in JOB_BEHAVIORS else 'Unknown'
            # TODO：这⾥的埋点记录⾏为，涉及DB操作，会影响接⼝响应时间，能否改为异步记录？ 参考Celery异步任务
            # 根据 api_category 和 api_name 记录请求次数
            api_request_count, _ =ApiRequestCount.objects.get_or_create(api_category=api_category, api_name=api_name)
            api_request_count.request_count = F("request_count") + 1
            api_request_count.save()
        except Exception as e:  # pylint: disable=broad-except
            logger.exception(f"Unexpected Exception when record user behavior:{e}")
            pass
        return None
