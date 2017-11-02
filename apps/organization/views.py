#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import PageNotAnInteger,Paginator

from .models import CourseOrg, CityDict, Teacher
from .forms import UserAskForm
# Create your views here.
class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("click_nums")[:3]

        #城市
        all_citys = CityDict.objects.all()

        #取出筛选培训结构
        org_type = request.GET.get('ct', '')
        if org_type:
            all_orgs = all_orgs.filter(catgory=org_type)

        #取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        sort = request.GET.get('sort', "")
        if sort:
            all_orgs = all_orgs.order_by('-'+sort)

        org_nums = all_orgs.count()

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 3, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_num": org_nums,
            "city_id": city_id,
            "org_type": org_type,
            "hot_orgs": hot_orgs,
            "sort": sort
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status':'sucess'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail', 'msg':'添加出错'}", content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """
    def get(sel, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-homepage.html',{
            "all_courses": all_courses,
            "all_teachers": all_teachers
        })