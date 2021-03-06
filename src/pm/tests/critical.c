/****************************************************************************
*
*                   SciTech OS Portability Manager Library
*
*  ========================================================================
*
*   Copyright (C) 1991-2004 SciTech Software, Inc. All rights reserved.
*
*   This file may be distributed and/or modified under the terms of the
*   GNU General Public License version 2.0 as published by the Free
*   Software Foundation and appearing in the file LICENSE.GPL included
*   in the packaging of this file.
*
*   Licensees holding a valid Commercial License for this product from
*   SciTech Software, Inc. may use this file in accordance with the
*   Commercial License Agreement provided with the Software.
*
*   This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING
*   THE WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR
*   PURPOSE.
*
*   See http://www.scitechsoft.com/license/ for information about
*   the licensing options available and how to purchase a Commercial
*   License Agreement.
*
*   Contact license@scitechsoft.com if any conditions of this licensing
*   are not clear to you, or you have questions about licensing options.
*
*  ========================================================================
*
* Language:     ANSI C
* Environment:  any
*
* Description:  Test program to check the ability to install a C based
*               critical error handler.
*
*               Functions tested:   PM_installAltCriticalHandler()
*                                   PM_restoreCriticalHandler()
*
****************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include "pmapi.h"

int main(void)
{
    FILE    *f;
    int     axcode,dicode;

    PM_installCriticalHandler();
    printf("Critical Error handler installed - trying to read from A: drive...\n");
    f = fopen("a:\bog.bog","rb");
    if (f) fclose(f);
    if (PM_criticalError(&axcode,&dicode,1)) {
        printf("Critical error occured on INT 21h function %02X!\n",
            axcode >> 8);
        }
    else printf("Critical error was not caught!\n");
    PM_restoreCriticalHandler();
    return 0;
}
