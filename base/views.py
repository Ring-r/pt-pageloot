from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='start_date',
                description='Start date for the range in YYYY-MM-DD format',
                required=True,
                type=str
            ),
            OpenApiParameter(
                name='end_date',
                description='End date for the range in YYYY-MM-DD format',
                required=True,
                type=str
            ),
            OpenApiParameter(
                name='user',
                description='User ID to filter expenses by',
                required=True,
                type=int
            ),
        ],
        responses={200: ExpenseSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='by-date-range')
    def list_by_date_range(self, request):
        # - List by Date Range: Create an endpoint to list all expenses for a user within a specific date range.
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        user_id = request.query_params.get('user')

        if not start_date or not end_date:
            return Response(
                {"error": "start_date and end_date are required."},
                status=400
            )

        try:
            expenses = self.queryset.filter(
                Q(date__gte=start_date) & Q(date__lte=end_date) & Q(user_id=user_id)
            )
            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=400
            )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='month',
                description='Month in numeric format (1-12)',
                required=True,
                type=int
            ),
            OpenApiParameter(
                name='year',
                description='Year in numeric format (e.g., 2024)',
                required=True,
                type=int
            ),
            OpenApiParameter(
                name='user',
                description='User ID to filter expenses by',
                required=True,
                type=int
            ),
        ],
        responses={200: OpenApiTypes.OBJECT}
    )
    @action(detail=False, methods=['get'], url_path='category-summary')
    def category_summary(self, request):
        # - Category Summary: Add an endpoint that calculates and returns the total expenses per category for a given month for a user.
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        user_id = request.query_params.get('user')

        if not month or not year:
            return Response(
                {"error": "month and year are required."},
                status=400
            )

        try:
            month = int(month)
            year = int(year)
            if month < 1 or month > 12:
                raise ValueError("Invalid month")

            expenses = self.queryset.filter(
                date__year=year,
                date__month=month,
                user_id=user_id
            ).values('category').annotate(total=Sum('amount'))

            return Response(expenses)
        except ValueError:
            return Response(
                {"error": "Invalid month or year format. Use numeric values."},
                status=400
            )
