#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def main():
    teachers, answers = data_read( "teacher2.txt", "answer2.txt" )


def data_read( ft_name, fa_name ):
    teachers = np.array([] )
    answers =  np.array([] )

    ft = open( ft_name, mode = "r" )
    fa = open( fa_name, mode = "r" )

    ft_data_string = ft.readlines()
    fa_data_string = fa.readlines()

    for i in range( 0, len( ft_data_string ) ):
        fa_data = fa_data_string[i].replace( "\n", "" )
        answers = np.append( answers, float( fa_data ) )
        
        ft_data = ft_data_string[i].replace( "\n", "" )
        ft_data = ft_data.split( " " )

        for r in range( 0, len( ft_data ) ):
            teachers = np.append( teachers ,float( ft_data[r] ) )

    ft.close()
    fa.close()

    teachers = teachers.astype( np.float32 )
    answers = answers.astype( np.float32 )

    teachers = np.reshape( teachers, ( int( len( teachers ) / 3 ), 3 ) )
    answers = np.reshape( answers, ( len( answers ) , 1 ) )

    return teachers, answers

main()
