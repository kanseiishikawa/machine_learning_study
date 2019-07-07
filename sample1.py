#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def main():
    teachers, answers = data_read( "teacher1.txt", "answer1.txt" )
    print( answers )

def data_read( ft_name, fa_name ):
    teachers = np.array([] )
    answers =  np.array([] )

    ft = open( ft_name, mode = "r" )
    fa = open( fa_name, mode = "r" )

    ft_data_string = ft.readlines()
    fa_data_string = fa.readlines()

    for i in range( 0, len( ft_data_string ) ):
        fa_data = fa_data_string[i].replace( "\n", "" )
        fa_data = fa_data.split( " " )

        for r in range( 0, len( fa_data ) ):
            answers = np.append( answers, float( fa_data[r] ) )
        
        ft_data = ft_data_string[i].replace( "\n", "" )
        ft_data = ft_data.split( " " )

        for r in range( 0, len( ft_data ) ):
            teachers = np.append( teachers ,float( ft_data[r] ) )

    ft.close()
    fa.close()

    teachers = teachers.astype( np.float32 )
    answers = answers.astype( np.float32 )

    teachers = np.reshape( teachers, ( int( len( teachers ) / 3 ), 3 ) )
    answers = np.reshape( answers, ( int( len( answers ) / 3 ), 3 ) )

    set_answers = np.array( [] )

    for i in range( 0, len( answers ) ):
        set_answers = np.append( set_answers, np.argmax( answers[i] ) )

    set_answers = set_answers.astype( np.int32 )


    return teachers, set_answers

main()
