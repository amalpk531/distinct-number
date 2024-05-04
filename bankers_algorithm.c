#include <stdio.h>
void main()
{
    int n, m, max[10][10], allo[10][10], avail[10], i, j, k, y;
    printf("No of process");
    scanf("%d", &n);
    printf("no of resource");
    scanf("%d", &m);
    printf("max ");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &max[i][j]);
        }
    }
    printf("allocated");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &allo[i][j]);
        }
    }
    printf("Available");
    for (i = 0; i < m; i++)
    {
        scanf("%d", &avail[i]);
    }
    int finish[n], safe[n], work[m], need[n][m], ind = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - allo[i][j];
        }
    }
    printf("need matrix is:");
    for (i = 0; i < n; i++)
    {
        printf("\n");
        for (j = 0; j < m; j++)
        {
            printf("%d\t", need[i][j]);
        }
    }
    for (i = 0; i < n; i++)
    {
        work[i] = avail[i];
        finish[i] = 0;
    }
    for (k = 0; k < n; k++)
    {
        for (i = 0; i < n; i++)
        {
            if (finish[i] == 0)
            {
                int flag = 0;
                for (j = 0; j < m; j++)
                {
                    if (need[i][j] > work[j])
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                {
                    safe[ind++] = i;
                    for (y = 0; y < m; y++)
                    {
                        work[y] += allo[i][y];
                        finish[i] = 1;
                    }
                }
            }
        }
    }

}
