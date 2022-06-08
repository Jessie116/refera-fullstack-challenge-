export const categoryColumns = [
    { field: "id", headerName: "ID", width: 70 },
   
    
      {
        field: "name",
        headerName: "name",
        width: 200,
      },

      {
        field: "status",
        headerName: "Status",
        width: 160,
        renderCell: (params) => {
          return (
            <div className={`cellWithStatus ${params.row.status}`}>
              {params.row.status}
            </div>
          );
        },
      },
   
  ];
  
  //temporary data
  export const categoryRows = [
    {
      id: 1,
      name: "Hidraulica",
      status: "active",
    }
  ];
  