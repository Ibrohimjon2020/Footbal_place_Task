from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Faqat admin huquqiga ega bo'lgan foydalanuvchilarga ruhsat beriladi
        return request.user and request.user.role == 'admin'

class MaydonEgasiPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Maydon egasi bo'lgan foydalanuvchilarga faqat o'zining maydonini ko'rish va o'zgartirish huquqi beriladi
        return request.user and request.user.role == 'maydon_egasi'

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Oddiy foydalanuvchilarga faqat maydonlarni ko'rish va buyurtma qilish huquqi beriladi
        return request.user and request.user.role == 'user'